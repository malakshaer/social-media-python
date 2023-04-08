import React, { useState } from "react";
import "./usersnavigation.css";
import FollowersList from "../FollowersList/FollowersList";
import FollowingList from "../FollowingList/FollowingList";
import RequestsList from "../RequestsList/RequestsList";
import RequestSentList from "../RequestSentList/RequestSentList";

const UsersNavigation = () => {
  const [listType, setListType] = useState("");
  const [isActive, setIsActive] = useState(false);

  const renderList = () => {
    switch (listType) {
      case "followers":
        return <FollowersList />;
      case "following":
        return <FollowingList />;
      case "requests":
        return <RequestsList />;
      case "sentRequests":
        return <RequestSentList />;
      default:
        return null;
    }
  };

  return (
    <div>
      <nav className="users-navigation">
        <div className="users-navigation-menu">
          <ul>
            <li>
              <button
                className={isActive ? "active" : ""}
                onClick={() => {
                  setIsActive(true);
                  setListType("followers");
                }}
              >
                Followers
              </button>
            </li>
            <li>
              <button
                className={isActive ? "active" : ""}
                onClick={() => {
                  setIsActive(true);
                  setListType("following");
                }}
              >
                Following
              </button>
            </li>
            <li>
              <button
                className={isActive ? "active" : ""}
                onClick={() => {
                  setIsActive(true);
                  setListType("requests");
                }}
              >
                Requests List
              </button>
            </li>
            <li>
              <button
                className={isActive ? "active" : ""}
                onClick={() => {
                  setIsActive(true);
                  setListType("sentRequests");
                }}
              >
                Sent Requests
              </button>
            </li>
          </ul>
        </div>
      </nav>
      {renderList()}
    </div>
  );
};

export default UsersNavigation;
