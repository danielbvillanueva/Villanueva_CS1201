<p align="center">
  <img src="images/CalculatorBanner.jpg" style="max-width: 600px; height: auto;" alt="GUI Calculator">
</p>

## 🧮 About
**GUI Calculator** is a Windows Forms application built using C#. It allows users to perform basic arithmetic operations through a user-friendly interface. This calculator supports real-time expression building, sign switching, decimal inputs, and error handling—all while showcasing core object-oriented principles and event-driven programming.

## 📔 Table of Contents
- [Features](#features)
- [OOP Principles](#oop-principles)
- [How to Run](#how-to-run)
- [File Structure](#file-structure)
- [Screenshots](#screenshots)
- [Members](#members)
- [Acknowledgements](#acknowledgements)

## <a id="features">🔢 Features</a>
- Add, subtract, multiply, and divide
- Real-time expression building
- Delete individual characters
- Clear current or all input
- Sign change button (+/-)
- Decimal point support
- Error handling for invalid inputs and math errors
- Expression preview display

## <a id="oop-principles">⚖️ OOP Principles Used</a>

### 🔐 Encapsulation
All calculator logic (state, current expression, and UI behavior) is encapsulated inside the `Form1` class. Fields like `expression`, `resultValue`, and flags like `justEvaluated` are private and managed only through methods.

### 📦 Abstraction
UI buttons (numbers, operators) use delegated methods like `NumberButton_Click` and `Operator_Click`, abstracting the click behavior through centralized functions.

### 🧠 Event-Driven Logic
The calculator registers all button click events at runtime using the `RegisterEvents()` method, ensuring maintainable and scalable code.

## <a id="how-to-run">⚙️ How to Run</a>

1. Clone or download the repository.
2. Open the `.sln` file in Visual Studio.
3. Ensure all resources and image files are present in the project.
4. Build and run the application.
5. Use the calculator with your mouse or keyboard (if extended).

## <a id="file-structure">📁 File Structure</a>

```
├── bin/Debug
│   └── CalculatorAppLab4.exe
├── images/
│   └── CalculatorBanner.jpg
├── Form1.cs          # Contains full calculator logic and event handling
├── Form1.Designer.cs # Auto-generated layout file
├── Program.cs        # Application entry point
├── CalculatorAppLab4.csproj
├── README.md
```

## <a id="screenshots">📸 Screenshots</a>

<p align="center">
  <img src="images/CalculatorUI.png" style="max-width: 600px; height: auto;" alt="Main UI">
</p>

<p align="center">
  <img src="images/CalculatorWithExpression.png" style="max-width: 600px; height: auto;" alt="Expression Example">
</p>

## <a id="members">👥 Group Members</a>

| Name | SR-Code | 
|------|---------|
| [Calog, Chester King](https://github.com/ChesterCalog) | 23-09045 |   
| [Donayre, Aila Roshiele](https://github.com/ailadonayre) | 23-02175 |  
| [Villanueva, Daniel](https://github.com/danielbvillanueva) | 23-01037 | 
| [Tarcelo, Mark Niño](https://github.com/ElgatoMe0w) | 20-08675 | 

## <a id="acknowledgements">💎 Acknowledgements</a>
Special thanks to our instructor, **Ms. Fatima Marie Agdon**, for guiding us through event-driven programming and WinForms development. This project enhanced our understanding of C# and GUI applications.
