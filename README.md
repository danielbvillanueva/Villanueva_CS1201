<p align="center">
  <img src="images/Calculator_Main_Banner.jpg" style="max-width: 600px; height: auto;" alt="GUICalculator">
</p>

# 🧮 GUI Calculator - C# WinForms

## 🌟 About
**GUI Calculator** is a beginner-friendly Windows Forms (WinForms) application developed using C#. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division through a user-friendly graphical interface. This project demonstrates the use of **object-oriented programming (OOP)** concepts like **encapsulation** and **abstraction**, along with event-driven design in C#.

---

## 📔 Table of Contents
- [🎯 Program Features](#-program-features)
- [⚖️ OOP Principles Used](#️-oop-principles-used)
- [⚙️ Instructions to Run the App](#️-instructions-to-run-the-app)
- [📁 File Structure](#-file-structure)
- [🛠️ Sample Output](#️-sample-output)
- [📸 Project Screenshots](#-project-screenshots)
- [👥 Group Members](#-group-members)
- [💎 Acknowledgements](#-acknowledgements)

---

## 🎯 Program Features
- Clean and responsive Windows Forms user interface
- Performs:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Prevents divide-by-zero errors
- Separated UI and logic using modular code design
- Instant display of calculation results

---

## ⚖️ OOP Principles Used

### 🔐 Encapsulation
Encapsulation means hiding the internal state and requiring interaction through public methods.

✅ **In This Project:**  
All arithmetic operations are encapsulated within the `Calculator` class. This protects internal logic and provides clean access through public methods only.

```csharp
public class Calculator
{
    public double Add(double a, double b) => a + b;
    public double Subtract(double a, double b) => a - b;
    public double Multiply(double a, double b) => a * b;

    public double Divide(double a, double b)
    {
        if (b == 0)
            throw new DivideByZeroException("Cannot divide by zero.");
        return a / b;
    }
}
```

### 🧼 Abstraction
Abstraction allows users to interact with a simplified interface without knowing the underlying implementation.

✅ **In This Project:**  
The `Form1.cs` UI interacts with `Calculator` without knowing how operations are computed. Users just press buttons to perform operations.

---

## ⚙️ Instructions to Run the App

1. Clone or download the repository.
2. Open the solution (`CalculatorApp.sln`) in **Visual Studio**.
3. Build the project using **Build > Build Solution** or `Ctrl + Shift + B`.
4. Run the app using **Debug > Start Debugging** or `F5`.
5. Use the calculator buttons to perform basic arithmetic.

---

## 📁 File Structure
```
├── bin/Debug/net9.0-windows
│   └── CalculatorApp.exe     # Compiled application
├── images/                   # Screenshots and banner for README
├── Calculator.cs             # Contains core calculator logic
├── Form1.cs                  # Handles button click logic (UI logic)
├── Form1.Designer.cs         # Contains the visual layout (auto-generated)
├── CalculatorApp.csproj
├── CalculatorApp.sln
├── Program.cs                # Application entry point
├── README.md                 # Project documentation
```

---

## 🛠️ Sample Output
```plaintext
+-------------------------+
|       45 + 77          |
|------------------------|
|        = 122           |
+-------------------------+

+-------------------------+
|       9 / 0            |
|------------------------|
|    Error: Cannot divide
     by zero.            |
+-------------------------+
```

---

## 📸 Project Screenshots

<p align="center">
  <img src="images/MainInterface.png" style="max-width: 600px; height: auto;" alt="Calculator Main Interface">
</p>
<p align="center">
  <img src="images/AdditionExample.png" style="max-width: 600px; height: auto;" alt="Addition Example">
</p>
<p align="center">
  <img src="images/ErrorHandling.png" style="max-width: 600px; height: auto;" alt="Divide by Zero Error">
</p>

---

## 👥 Group Members

| Name | SR-Code | 
|------|---------|
| [Calog, Chester King](https://github.com/ChesterCalog) | 23-09045 |   
| [Donayre, Aila Roshiele](https://github.com/ailadonayre) | 23-02175 |  
| [Villanueva, Daniel](https://github.com/danielbvillanueva) | 23-01037 | 
| [Tarcelo, Mark Niño](https://github.com/ElgatoMe0w) | 20-08675 | 

---

## 💎 Acknowledgements
Special thanks to our instructor, **Ms. Fatima Marie Agdon**, for guiding us in developing a WinForms project in C#. Through this GUI calculator, we practiced combining OOP concepts with user interface programming.

---
