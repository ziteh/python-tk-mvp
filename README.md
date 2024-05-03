# Python Tkinter MVP

An example of MVP (Model-View-Presenter) pattern implementation with Python [Tkinter](https://docs.python.org/3/library/tkinter.html).

## Usage

```bash
python main.py
```

## UML Class Diagram

```mermaid
---
title: Tk MVP
---
classDiagram
    direction TB

    class PresenterInterface {
        <<interface>>
        on_click()
        on_select(float)
    }
    class Presenter {
        -model: Model
        -view: ViewInterface
        +Presenter(Model, ViewInterface)
        +on_click()
        +on_select(float)
    }

    class ViewInterface {
        <<interface>>
        setup(PresenterInterface)
        set_value(float)
        get_value() float
    }
    class View {
        -root: tk.Tk
        -presenter: PresenterInterface
        +View(tk.Tk)
        +setup(PresenterInterface)
        +set_value(float)
        +get_value() float 
    }

    class Model {
        -data: float
        +set_data(float)
        +get_data() float
    }

    PresenterInterface --o View : Aggregation
    ViewInterface <|.. View : Implementation
    ViewInterface --o Presenter : Aggregation
    PresenterInterface <.. ViewInterface : Use
    PresenterInterface <|.. Presenter : Implementation
    Model --o Presenter : Aggregation
```
