import React from "react";
import Navbar from "../../components/Navbar/Navbar";
import profileImage from "../../assets/profileImage.png";
import UsersNavigation from "../../components/UsersNavigation/UsersNavigation";
import "./profile.css";
import FollowersList from "../../components/FollowersList/FollowersList";

const Profile = () => {
  return (
    <div>
      <Navbar />
      <div>
        <div className="profile-face">
          <img src={profileImage} alt="" />
          <p>Malak Shaer</p>
        </div>
        <div>
          <UsersNavigation />
          <FollowersList />
        </div>
      </div>
    </div>
  );
};

export default Profile;
