Bitcoin Sentiment Analysis & Trader Behavior
📈 Project Overview
This comprehensive analysis examines the intricate relationship between Bitcoin market sentiment and trader performance using the Bitcoin Fear & Greed Index and Hyperliquid trading data. By systematically linking sentiment phases with trader profitability, leverage patterns, and trade volume dynamics, the research identifies significant trends and evaluates potential contrarian trading strategies.



🎯 Key Objectives
Quantify Profitability Differentials between Fear versus Greed market periods

Examine Leverage Utilization and position bias across sentiment phases

Identify Contrarian Signals for strategic trading opportunities

Analyze Behavioral Patterns of traders during extreme sentiment conditions

🛠 Technical Stack
Python 3 – Core programming language for analysis

Pandas – Data preprocessing and analytical operations

NumPy – Numerical computations and mathematical operations

Matplotlib / Seaborn – Data visualization and graphical representation

Jupyter Notebook / Google Colab – Interactive development environment

⚙️ Installation & Setup
Repository Cloning
bash
git clone https://github.com/akashgadde05/Bitcoin-Sentiment-Trading.git
cd Bitcoin-Sentiment-Trading
Virtual Environment Configuration (Recommended)
bash
# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate        # Linux/MacOS
venv\Scripts\activate          # Windows
Dependency Installation
bash
pip install -r requirements.txt
Execution
Launch notebook_1.ipynb in Jupyter Notebook or Google Colab environment and execute cells sequentially.

💾 Dataset Description
Bitcoin Sentiment Data (bitcoin_sentiment.csv)
Date – Temporal reference for sentiment measurement

Fear/Greed Classification – Daily market sentiment categorization

Provides continuous sentiment index tracking (Fear or Greed classification)

Trader Activity Data (trader_data.csv)
Account – Unique trader identifier

Symbol – Trading instrument specification

Price – Transaction execution price

Size – Trade volume magnitude

Side – Position direction (Long/Short)

Time – Transaction timestamp

PnL – Profit and Loss realization

Leverage – Position leverage multiplier

Contains comprehensive trading history sourced from Hyperliquid platform

Integration Note: Both datasets undergo temporal merging based on date fields to enable sentiment-trade relationship analysis.

🧾 Analytical Framework & Features
1. Sentiment Distribution Analysis
Quantitative assessment of Fear versus Greed day classification

Temporal distribution patterns of market sentiment

2. Trading Activity Profiling
Aggregate trade volume and frequency metrics

Unique trader participation analysis

Primary trading instrument concentration

3. Profit & Loss Distribution
PnL dispersion characteristics across trader population

Statistical analysis of profitability patterns

4. Leverage Utilization Patterns
Risk exposure assessment during different sentiment phases

Leverage magnitude correlation with market sentiment

5. Position Bias Examination
Long versus Short position preference relative to sentiment

Behavioral inclination shifts across sentiment regimes

6. Correlation Structure Analysis
Multivariate relationships between PnL, leverage, and volume metrics

Sentiment impact quantification on trading parameters

7. Trader Segmentation Framework
Performance-based categorization (winners, losers, volatile traders)

Behavioral clustering according to sentiment response

8. Contrarian Strategy Exploration
Profitability assessment of "buy fear / sell greed" approaches

Counter-trend trading opportunity identification

🖼 Analytical Visualizations
(Visualization placeholders for generated analytical plots)

sentiment_distribution.png – Market sentiment temporal overview

pnl_distribution.png – Profit & loss statistical distribution

leverage_patterns.png – Average leverage utilization per sentiment phase

position_bias.png – Long versus Short position allocation by sentiment

correlation_matrix.png – Multivariate correlation analysis of trading metrics

🔍 Key Analytical Insights
Profitability Dynamics: Traders demonstrate [increased/decreased] profitability during Fear-dominated periods compared to Greed phases

Leverage Behavior: Average leverage utilization exhibits [ascending/descending] patterns during Greed market conditions

Contrarian Potential: Strategic approaches incorporating sentiment extremes show promising alpha generation capabilities

Psychological Influence: Position bias demonstrates measurable shifts corresponding to sentiment fluctuations, indicating behavioral finance impacts

📁 Repository Architecture
text
Bitcoin-Sentiment-Trading/
├── notebook_1.ipynb              # Primary analytical notebook
├── bitcoin_sentiment.csv         # Market sentiment dataset
├── trader_data.csv               # Trader activity dataset
├── README.md                     # Comprehensive project documentation
├── requirements.txt              # Python dependency specification
├── Outputs/                      # Generated analytical visualizations
│   ├── sentiment_distribution.png
│   ├── pnl_distribution.png
│   ├── leverage_patterns.png
│   ├── position_bias.png
│   └── correlation_matrix.png
└── csv_files/                    # Processed intermediate datasets
    ├── merged_data.csv
    ├── trader_segmentation.csv
    └── sentiment_summary.csv


👨‍💻 Author Information
Akash Gadde

Email: akashgadde05@gmail.com

GitHub: https://github.com/akashgadde05

Project Repository: Bitcoin-Sentiment-Trading