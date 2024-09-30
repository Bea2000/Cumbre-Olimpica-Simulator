# Cumbre Olímpica Simulator

This project is a simulation of an Olympic competition where teams of athletes from different delegations compete in various sports disciplines. The simulation models different aspects such as athlete training, competitions, injuries, and the performance of the delegations they represent. This project was developed during the second semester of 2020 as part of my second-year Civil Engineering studies at Pontificia Universidad Católica de Chile.

## Table of Contents

- [Cumbre Olímpica Simulator](#cumbre-olímpica-simulator)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Entities](#entities)
    - [Delegations](#delegations)
    - [Athletes](#athletes)
    - [Sports](#sports)
    - [Championship](#championship)
  - [Execution](#execution)
    - [Steps to Execute](#steps-to-execute)
    - [Required Files](#required-files)
  - [Usage Examples](#usage-examples)
  - [Expected Output](#expected-output)
  - [Conclusion](#conclusion)

## Overview

The **Cumbre Olímpica Simulator** is a command-line application that allows users to simulate competitions between different delegations of athletes. Each delegation has its own strengths and weaknesses, and athletes can compete in four sports: athletics, cycling, gymnastics, and swimming. The game includes object-oriented programming principles such as inheritance, polymorphism, and abstraction to represent the various entities in the simulation.

## Features

- **Delegations**: Manage athletes, train them, heal injuries, and compete in different sports.
- **Athletes**: Each athlete has attributes such as speed, resistance, flexibility, and morale, which influence their performance in the competitions.
- **Competitions**: Simulate daily competitions in different sports and track which athletes win medals.
- **Sports**: Include athletics, cycling, gymnastics, and swimming, each with specific attributes and competition rules.

## Entities

### Delegations

- **Attributes**: Includes coach, team, medals, morale, and money.
- **Actions**: Recruit athletes, train athletes, heal injuries, and use special abilities.
- **Types of Delegations**:
  - **IEEEsparta**: Stronger athletes with a special ability to boost morale.
  - **DCCrotona**: Athletes with enhanced flexibility, able to win medals easily.

### Athletes

- **Attributes**: Speed, resistance, flexibility, morale, injury status, and price.
- **Actions**: Train for competitions, participate in sports, and risk injury during competition.

### Sports

- **Attributes**: Includes whether equipment is required and the risk of injury.
- **Disciplines**: Athletics, cycling, gymnastics, and swimming.

### Championship

- Organizes and manages the competition between delegations and determines the overall winner.

## Execution

To run the **Cumbre Olímpica Simulator**, you need to execute the Python script in a terminal environment. Make sure that you have Python 3 installed on your machine.

### Steps to Execute

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/repo-url.git
    ```

2. Navigate to the project directory:

3. Run the main Python script:

    ```bash
    python3 main.py
    ```

### Required Files

- **`delegaciones.csv`**: A file containing information about the delegations.
- **`deportistas.csv`**: A file containing information about the athletes.
- **`resultados.txt`**: This file will store the results of each competition.

## Usage Examples

Here are some examples of how to interact with the program:

1. **Start a new competition day**:
    - The program will prompt you to choose athletes to compete in each sport for the day. You can choose one athlete from each delegation.
    - Competitions will be simulated automatically, and results will be stored in `resultados.txt`.

2. **View the status of the competition**:
    - This option will display the status of all delegations, including information about the athletes, the number of medals won, and the current morale of each delegation.

3. **Train athletes**:
    - Before competitions, you can choose to train your athletes in various attributes, such as speed or resistance, which can improve their chances of winning.

## Expected Output

The expected output will vary based on the actions taken during the game. Some examples of output include:

1. **Results of the competition day**:

    ```bash
    Day 1 Results:
    Athletics - Winner: IEEEsparta - Athlete: Juan Perez
    Cycling - Winner: DCCrotona - Athlete: Maria Gonzalez
    Gymnastics - Winner: DCCrotona - Athlete: Anna Smith
    Swimming - Winner: IEEEsparta - Athlete: Carlos Ruiz
    ```

2. **Status of delegations**:

    ```bash
    Delegation: IEEEsparta
    Medals: 3
    Morale: 75
    Athletes:
      - Juan Perez (Speed: 85, Resistance: 90, Flexibility: 60)
      - Carlos Ruiz (Speed: 88, Resistance: 78, Flexibility: 85)
    ```

3. **Training athletes**:

    ```bash
    Athlete Juan Perez has increased his speed by 5 points!
    ```

## Conclusion

The **Cumbre Olímpica Simulator** allows for an engaging simulation of a sports championship where users can manage their delegations, train athletes, and compete in various sports. It highlights the use of object-oriented programming concepts such as inheritance, polymorphism, and abstract classes, making it a comprehensive project that covers key programming fundamentals.
