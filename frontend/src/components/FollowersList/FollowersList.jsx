import { Users } from "../../users";
import User from "../User/User";
import "./followerslist.css";

const FollowersList = () => {
  return (
    <div className="users-cart">
      {Users.map((user) => (
        <User key={user._id} data={user} />
      ))}
    </div>
  );
};

export default FollowersList;
