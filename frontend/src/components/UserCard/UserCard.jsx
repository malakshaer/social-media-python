import React from "react";
import "./usercard.css";
import axios from "axios";
import Button from "../Button/Button";

const UserCard = ({ data }) => {
  const { _id, firstName, lastName, bio, num_followers, num_following } = data;

  const handleFollow = () => {
    axios
      .post(`follow/${_id}`)
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className="card" style={{ width: "200px" }}>
      <div className="card-body">
        <h5 className="card-title">{`${firstName} ${lastName}`}</h5>
        <span>{`${bio}`}</span>
        <div className="count">
          <p className="card-text">Followers: {num_followers}</p>
          <p className="card-text">Following: {num_following}</p>
        </div>
        <Button text={"Follow"} onClick={handleFollow} />
      </div>
    </div>
  );
};

export default UserCard;
