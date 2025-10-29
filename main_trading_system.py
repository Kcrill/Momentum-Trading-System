import sys
import os
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from strategy.momentum_strategy import get_momentum_signals
from execution.webull_trader import WebullPaperTrader


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('trading_system.log'),
            logging.StreamHandler()
        ]
    )


def run_complete_trading_cycle():
    print("=" * 60)
    print(">>> MOMENTUM TRADING SYSTEM - COMPLETE CYCLE")
    print("=" * 60)
    
    print("\n1. INITIALIZING COMPONENTS...")
    trader = WebullPaperTrader()
    
    print("\n2. CHECKING ACCOUNT...")
    account_info = trader.get_paper_trading_info()
    
    print("\n3. GENERATING MOMENTUM SIGNALS...")
    signals = get_momentum_signals()
    
    if signals is None or len(signals) == 0:
        print(">>> ERROR: No signals generated - stopping")
        return
    
    trading_signals = []
    for symbol, momentum in signals.items():
        trading_signals.append({
            'symbol': symbol,
            'momentum_score': momentum
        })
    
    print(f">>> SUCCESS: Generated {len(trading_signals)} trading signals")
    
    print("\n4. EXECUTING TRADES...")
    portfolio_value = 10000
    executed_trades = trader.execute_strategy_signals(trading_signals, portfolio_value)
    
    print("\n5. TRADING CYCLE SUMMARY")
    print("=" * 40)
    print(f"Signals Generated: {len(trading_signals)}")
    print(f"Trades Executed: {len(executed_trades)}")
    print(f"Portfolio Value: ${portfolio_value:,}")
    print("=" * 40)
    
    if executed_trades:
        print("\nEXECUTED TRADES:")
        for trade in executed_trades:
            print(f"   - {trade['symbol']}: {trade['shares']} shares")
    
    print("\n>>> TRADING CYCLE COMPLETE!")


def main():
    print(">>> MOMENTUM TRADING SYSTEM STARTING...")
    print("This system will:")
    print("  1. Calculate 12-month momentum signals")
    print("  2. Select top 2 performing stocks") 
    print("  3. Execute paper trades in Webull")
    print("  4. Log all activity")
    print()
    
    try:
        run_complete_trading_cycle()
    except Exception as e:
        print(f">>> SYSTEM ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()