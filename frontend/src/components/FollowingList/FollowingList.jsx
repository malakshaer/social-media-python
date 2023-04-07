import { Users } from "../../users";
import User from "../User/User";
import "./followinglist.css";

const FollowingList = () => {
  return (
    <div className="users-card">
      {Users.map((user) => (
        <User key={user._id} data={user} textButton="unfollow" />
      ))}
    </div>
  );
};

export default FollowingList;
