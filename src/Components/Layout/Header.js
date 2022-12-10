import React from "react";
import mealsImage from "../../assets/meals.jpg";
import classes from "./Header.module.css";

import { HeaderCartButton } from "./HeaderCartButton";
export const Header = (props) => {
  return (
    <React.Fragment>
      <header className={classes.header}>
        <h1>FoodDeed</h1>
        <HeaderCartButton onClick={props.onShowCart} />
      </header>
      <button>Cart</button>
      <div className={classes["main-image"]}>
        <img src={mealsImage} alt="table full delicious food" />
      </div>
    </React.Fragment>
  );
};
