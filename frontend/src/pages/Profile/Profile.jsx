import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "../../components/Navbar/Navbar";
import "./profile.css";
import UsersNavigation from "../../components/UsersNavigation/UsersNavigation";
import Button from "../../components/Button/Button";
import axios from "axios";
import profileImage from "../../assets/profileImage.png";

const Profile = () => {
  const navigate = useNavigate();
  const [user, setUser] = useState({
    firstName: "",
    lastName: "",
    numberFollowers: 0,
    numberFollowing: 0,
    bio: "",
    image: "",
  });

  useEffect(() => {
    const getProfile = async () => {
      try {
        const token = localStorage.getItem("token");
        const headers = {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        };

        const response = await axios.get("/get-user-info", { headers });
        console.log(response.data);
        const base64Image = `data:image/jpg;base64,${response.data.image}`;
        setUser({
          ...response.data,
          image: base64Image,
        });
      } catch (error) {
        console.log(error);
      }
    };

    getProfile();
  }, []);

  const handleEditAccount = () => {
    navigate("/edit-account");
  };

  return (
    <div>
      <Navbar />
      <div className="user-card">
        <div className="user-card-left">
          <img src={user.image || profileImage} alt="Profile" />
        </div>
        <div className="user-card-center">
          <p className="user-card-name">{`${user.firstName} ${user.lastName}`}</p>
          <span className="user-card-bio">{user.bio}</span>
          <p className="user-card-count">{`Followers: ${user.numberFollowers} | Following: ${user.numberFollowing}`}</p>
        </div>
        <div className="user-card-right">
          <Button text={"Edit Account"} onClick={handleEditAccount} />
        </div>
      </div>
      <UsersNavigation />
    </div>
  );
};

export default Profile;
