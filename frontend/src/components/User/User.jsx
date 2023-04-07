import React from "react";
import "./user.css";

const User = (props) => {
  const { firstName, lastName } = props.data;
  const { textButton } = props;

  const handleButton = () => {
    console.log("follow");
  };

  return (
    <div className="user">
      {/* <img src={userImage} alt="" /> */}
      <div className="username">
        <span>
          {firstName} {lastName}
        </span>
      </div>
      <button
        className="btn"
        onClick={() => {
          handleButton();
        }}
      >
        {textButton}
      </button>
    </div>
  );
};

export default User;
