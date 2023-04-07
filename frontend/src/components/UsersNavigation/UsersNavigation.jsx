import React from "react";
import "./usersnavigation.css";

const UsersNavigation = () => {
  return (
    <nav className="users-navigation">
      <div className="users-navigation-menu">
        <ul>
          <li>
            <a href="/">Followers</a>
          </li>
          <li>
            <a href="/">Following</a>
          </li>
          <li>
            <a href="/">Request List</a>
          </li>
          <li>
            <a href="/">Requested</a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default UsersNavigation;
