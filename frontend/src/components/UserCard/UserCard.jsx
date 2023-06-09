import React from "react";
import "./usercard.css";
import axios from "axios";
import Button from "../Button/Button";

const UserCard = ({
  data,
  firstName,
  lastName,
  bio,
  numberFollowers = 0,
  numberFollowing = 0,
  image,
}) => {
  const { _id } = data;

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
        <img src={image} alt="" />
        <h5 className="card-title">{`${firstName} ${lastName}`}</h5>
        <span>{`${bio}`}</span>
        <div className="count">
          <p className="card-text">Followers: {numberFollowers}</p>
          <p className="card-text">Following: {numberFollowing}</p>
        </div>
        <Button text={"Follow"} onClick={handleFollow} />
      </div>
    </div>
  );
};

export default UserCard;
