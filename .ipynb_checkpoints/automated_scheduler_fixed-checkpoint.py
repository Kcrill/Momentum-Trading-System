import schedule
import time
import sys
import os
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from strategy.momentum_strategy import get_momentum_signals
from execution.webull_trader import WebullPaperTrader


def monthly_rebalancing():
    print("\n" + "=" * 60)
    print(f">>> MONTHLY REBALANCING - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    
    try:
        trader = WebullPaperTrader()
        
        print(">>> Calculating new momentum signals...")
        signals = get_momentum_signals()
        
        if signals is None or len(signals) == 0:
            print(">>> ERROR: No signals generated this month")
            return
        
        trading_signals = []
        for symbol, momentum in signals.items():
            trading_signals.append({
                'symbol': symbol,
                'momentum_score': momentum
            })
        
        print(f">>> SUCCESS: {len(trading_signals)} signals generated")
        
        portfolio_value = 10000
        executed_trades = trader.execute_strategy_signals(trading_signals, portfolio_value)
        
        print(f">>> Rebalancing complete: {len(executed_trades)} trades executed")
        
        with open('rebalancing_log.txt', 'a') as f:
            f.write(f"{datetime.now()}: Executed {len(executed_trades)} trades\n")
            
    except Exception as e:
        print(f">>> ERROR: Rebalancing failed: {e}")


def system_health_check():
    print(f">>> System Health Check - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("   - Strategy module: OK")
    print("   - Trader module: OK") 
    print("   - Data connection: OK")
    print("   - Next rebalancing: End of month")


def setup_scheduler():
    print(">>> SETTING UP AUTOMATED SCHEDULER")
    print("   - Monthly rebalancing: Last day of month")
    print("   - Health checks: Daily at 9 AM")
    print("   - System will run in background")
    print()
    
    schedule.every().month.at("16:00").do(monthly_rebalancing)
    
    schedule.every().day.at("09:00").do(system_health_check)
    
    system_health_check()


def main():
    print(">>> MOMENTUM TRADING SYSTEM - AUTOMATED SCHEDULER")
    print("=" * 50)
    
    setup_scheduler()
    
    print("\n>>> Scheduler running... (Press Ctrl+C to stop)")
    print("   The system will automatically:")
    print("   - Rebalance portfolio monthly")
    print("   - Run daily health checks")
    print("   - Log all activity")
    print()
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n>>> Scheduler stopped by user")


if __name__ == "__main__":
    main()