import React, { useState, useEffect } from "react";
import User from "../User/User";
import "./followinglist.css";
import axios from "axios";
import Empty from "../Empty/Empty";

const FollowingList = () => {
  const [followings, setFollowings] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get("/get-following");
        const followingList = response.data.following.map((following) => {
          const base64Image = `data:image/jpg;base64,${following.image}`;
          return {
            id: following.id,
            name: following.name,
            image: base64Image,
          };
        });
        setFollowings(followingList);
      } catch (error) {
        console.log(error);
      }
    }
    fetchData();
  }, []);

  const handleUnFollow = async (userId) => {
    try {
      await axios.put(`/unfollow/${userId}`);
      setFollowings((prevFollowers) =>
        prevFollowers.filter((follower) => follower.id !== userId)
      );
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="users-card">
      {followings.length === 0 ? (
        <Empty />
      ) : (
        followings.map((user) => (
          <User
            key={user.id}
            name={user.name}
            image={user.image}
            textButton="unfollow"
            onClick={() => handleUnFollow(user.id)}
          />
        ))
      )}
    </div>
  );
};

export default FollowingList;
