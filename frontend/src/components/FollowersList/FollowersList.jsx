import React, { useState, useEffect } from "react";
import User from "../User/User";
import "./followerslist.css";
import axios from "axios";

const FollowersList = () => {
  const [followers, setFollowers] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get("/get-followers");
        const followersList = response.data.followers.map((follower) => {
          return {
            id: follower.id,
            name: follower.name,
          };
        });
        setFollowers(followersList);
      } catch (error) {
        console.log(error);
      }
    }
    fetchData();
  }, []);

  const handleRemoveFollower = async (userId) => {
    try {
      await axios.post(`/remove-follower/${userId}`);
      setFollowers((prevUser) =>
        prevUser.filter((follower) => follower.id !== userId)
      );
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="users-card">
      {followers.map((user) => (
        <User
          key={user.id}
          name={user.name}
          textButton="Remove"
          onClick={() => handleRemoveFollower(user.id)}
        />
      ))}
    </div>
  );
};

export default FollowersList;
