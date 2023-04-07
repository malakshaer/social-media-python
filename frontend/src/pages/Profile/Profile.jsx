import React from "react";
import Navbar from "../../components/Navbar/Navbar";
import profileImage from "../../assets/profileImage.png";
import "./profile.css";
import UsersNavigation from "../../components/UsersNavigation/UsersNavigation";

const Profile = () => {
  return (
    <div>
      <Navbar />
      <div>
        <div className="profile-face">
          <img src={profileImage} alt="" />
          <p>Malak Shaer</p>
        </div>
        <UsersNavigation />
      </div>
    </div>
  );
};

export default Profile;
