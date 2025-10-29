# Momentum Algorithmic Trading System

A quantitative trading platform that implements momentum-based investment strategies with automated execution and risk management.

## Project Overview

This system automatically identifies high-performing stocks using momentum factors and executes trades through Webull paper trading. The strategy selects top performers based on 12-month price momentum and rebalances the portfolio monthly.

### Key Features
- Momentum Strategy: 12-month cross-sectional momentum factor
- Automated Execution: Integrated with Webull API for paper trading  
- Risk Management: Position sizing and drawdown controls
- Scheduled Operation: Automated monthly rebalancing
- Production Architecture: Modular design with error handling

## Strategy Performance

- Backtested Returns: +1,403% total return
- Sharpe Ratio: 2.50 (risk-adjusted performance)
- Maximum Drawdown: -12.7% with risk management
- Win Rate: 66.2% monthly outperformance

## System Architecture

momentum_trading_system/
├── src/
│ ├── strategy/ # Momentum strategy logic
│ ├── execution/ # Webull trading interface
│ ├── risk/ # Risk management
│ └── utils/ # Utilities and helpers
├── main_trading_system.py # Complete trading system
├── automated_scheduler.py # Automated scheduling
└── requirements.txt # Python dependencies


## Strategy Details

Momentum Calculation

- Lookback Period: 12 months
- Universe: 21 diversified large-cap stocks
- Selection: Top 20% performers (4-5 stocks)
- Rebalancing: Monthly

Stock Universe

- Technology: AAPL. MSFT, GOOGL, AMZN, NVDA, META
- Healthcare: JNJ, UNH, LLY, PFE
- Consumer: PG, KO, PEP, WMT, COST. MCD
- Financials: JPM, V
- Energy/Industrials: XOM, CVX, HD

Development Resources

This project was developed with guidance from:
- Algorithmic trading concepts from "Advances in Financial Learning" by Marcos Lopez de Prado
- Momentum factor research from academic papers on cross-sectional momentum
- Webull API documentation for trade execution
- Python quantitative finance best practices

Risk Management

- Position sizing based on volatility
- Maximum drawdown limits
- Portfolio-level risk controls
- Individual trade risk management

Technical Stack

- Python 3.8+
- pandas, numpy for data analysis
- yfinance for market data
- webull-python for trading execution
- schedule for task automation

Important Disclaimer

    This software is for educational and research purposes only. Past performance does not guarantee future results. Trading securities involves risk and may not be suitable for all investors. Always conduct your own research and consider consulting with a qualified financial advisor before making investment decisions. 

License

    Mit License - see License file for details