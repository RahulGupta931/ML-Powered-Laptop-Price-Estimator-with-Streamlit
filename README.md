# 💻 Laptop Price Predictor

A machine learning-powered web application that predicts laptop prices based on specifications like brand, processor, RAM, storage, and display features.

## 🚀 Features

- **Interactive Web Interface**: User-friendly Streamlit app with organized input sections
- **Comprehensive Specifications**: Predict prices based on 12+ laptop features including:
  - Brand and laptop type
  - RAM, storage (HDD/SSD), and processor
  - Display specifications (size, resolution, touchscreen, IPS)
  - Graphics card and operating system
- **Real-time Predictions**: Instant price estimates with formatted currency display
- **Responsive Design**: Clean two-column layout for better user experience

## 📊 Model Features

- **Advanced Feature Engineering**: Includes PPI (pixels per inch) calculation for display quality
- **Categorical Encoding**: Handles brand names, processor types, and OS variations
- **Logarithmic Transformation**: Uses exponential conversion for accurate price predictions  

## 📁 Dataset  
The dataset contains laptop specifications and their corresponding prices with features including:
- **Company**: Brand names (Dell, HP, Apple, etc.)
- **TypeName**: Laptop categories (Gaming, Ultrabook, Workstation, etc.)
- **RAM**: Memory capacity (2GB to 64GB)
- **Weight**: Physical weight of the laptop
- **Display**: Screen size, resolution, touchscreen, and IPS capabilities
- **Processor**: CPU brand and specifications
- **Storage**: HDD and SSD capacities
- **Graphics**: GPU brand and type
- **Operating System**: Windows, macOS, Linux variants

## 🛠️ Technologies Used  
- **Language**: Python 3.x
- **Web Framework**: Streamlit
- **ML Libraries**: Scikit-learn, NumPy, Pandas
- **Model Persistence**: Pickle
- **Development**: Jupyter Notebook  

## 🤖 Model Architecture

The prediction pipeline includes:
- **Feature Engineering**: PPI calculation from screen resolution and size
- **Categorical Encoding**: Brand, processor, and OS encoding
- **Preprocessing Pipeline**: Integrated scaling and transformation
- **Model**: Trained regression model with logarithmic price transformation

## 📈 Model Performance

- Trained on comprehensive laptop dataset with 12 key features
- Uses exponential transformation for accurate price scaling
- Handles diverse laptop categories from budget to high-end gaming machines

## 🚀 Quick Start

### Prerequisites
```bash
pip install streamlit numpy pickle-mixin
```

### Running the Application

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd laptop-price-predictor
   ```

2. **Ensure model files are present**:
   - `pipe.pkl` (trained model pipeline)
   - `laptop.pkl` (dataset for dropdown options)

3. **Launch the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to `http://localhost:8501`

## 💡 Usage

1. Select your laptop specifications using the interactive form
2. Choose from organized categories:
   - **Basic Specs**: Brand, type, RAM, weight, CPU, OS
   - **Display & Storage**: Screen features, resolution, storage options, GPU
3. Click "🔮 Predict Price" to get an instant price estimate
4. View the formatted price prediction with currency formatting

## 📁 Project Structure

```
laptop-price-predictor/
├── app.py                          # Streamlit web application
├── pipe.pkl                        # Trained model pipeline
├── laptop.pkl                      # Dataset for UI options
├── laptop_data.csv                 # Raw dataset
├── Laptop_Price_Predictor.ipynb    # Model training notebook
└── README.md                       # Project documentation
```  
