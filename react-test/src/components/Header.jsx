import React, { Component } from "react";

export default class Header extends Component {
  render() {
    return (
      <header>
        <img
          style={{ marginTop: "-25px", width: "100px", position: "absolute" }}
          src={require("../assets/images/cat.gif")}
          alt="moving-cat"
        />
        <h1 style={{ marginTop: "0px", fontSize: "100px" }}>
          CA<span style={{ color: "gray", fontSize: "50px" }}>de</span>TBLUEE
        </h1>
      </header>
    );
  }
}
