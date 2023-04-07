import { Users } from "../../users";
import User from "../User/User";
import "./followerslist.css";

const FollowersList = () => {
  return (
    <div className="users-card">
      {Users.map((user) => (
        <User key={user._id} data={user} textButton="Remove" />
      ))}
    </div>
  );
};

export default FollowersList;
