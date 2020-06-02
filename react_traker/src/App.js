import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import * as Habits from "./habits.py";
//Надо вытащить данные из бд
const HABITS = [
  { name: "Palo Alto", zip: "94303" },
  { name: "San Jose", zip: "94088" },
  { name: "Santa Cruz", zip: "95062" },
  { name: "Honolulu", zip: "96803" }
];

class App extends Component {
  constructor() {
    super();
    this.state = {
      activeHabit: 0,
    };
  }
  render() {
    const activeHabit = this.state.activeHabit;
    return (
      <div className="App">
        {HABITS.map((habit, index) => (
          <button
            key={index}
            onClick={() => {
              this.setState({ activeHabit: index });
            }}
          >
              {habit.name}
          </button>
        ))}
        <HabitDisplay
          key={activeHabit}
          zip={HABITS[activeHabit].zip}
        />
      </div>
    );
  }
}

class HabitDisplay extends Component {
  constructor() {
    super();
    this.state = {
      weatherData: null
    };
  }
  componentDidMount() {
    const zip = this.props.zip;
    const URL = "http://api.openweathermap.org/data/2.5/weather?q=" +
      zip +
      "&appid=b1b35bba8b434a28a0be2a3e1071ae5b&units=imperial";
    fetch(URL).then(res => res.json()).then(json => {
      this.setState({ weatherData: json });
    });
  }
  render() {
    const weatherData = this.state.weatherData;
    if (!weatherData) return <div>Loading</div>;
    return <div>{JSON.stringify(weatherData)}</div>;
  }
}


export default App;
