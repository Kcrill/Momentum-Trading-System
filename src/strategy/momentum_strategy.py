import yfinance as yf
import pandas as pd
from datetime import datetime

def get_momentum_signals():
    """Our simple momentum strategy that worked in Jupyter"""
    print("🔄 Calculating momentum signals...")
    
    # Our proven stock list from backtesting
    stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META']
    
    try:
        # Download 1 year of data
        data = yf.download(stocks, period='1y', auto_adjust=True)
        prices = data['Close']
        
        # Calculate 12-month momentum (our winning formula)
        momentum = (prices.iloc[-1] / prices.iloc[0]) - 1
        
        # Get top 2 performers (simplified version)
        top_stocks = momentum.nlargest(2)
        
        print("✅ Momentum signals calculated!")
        print("Top performers:")
        for stock, mom in top_stocks.items():
            print(f"   {stock}: {mom:.1%}")
            
        return top_stocks
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

# Test our function - THIS MUST BE AT THE OUTDENT LEVEL (not inside the function)
if __name__ == "__main__":
    print("🧪 Testing our momentum strategy...")
    signals = get_momentum_signals()
    print("🎯 Strategy test complete!")
