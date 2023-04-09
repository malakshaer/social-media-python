import React from "react";
import "./user.css";

const User = ({ name, image, textButton, onClick }) => {
  return (
    <div className="user">
      <img src={image} alt="" />
      <div className="username">
        <span>{name}</span>
      </div>
      <button className="btn" onClick={onClick}>
        {textButton}
      </button>
    </div>
  );
};

export default User;
