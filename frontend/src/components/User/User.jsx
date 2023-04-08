import React from "react";
import "./user.css";

const User = ({ name, textButton, onClick }) => {
  return (
    <div className="user">
      {/* <img src={userImage} alt="" /> */}
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
