import { Users } from "../../users";
import User from "../User/User";
import "./requestsentlist.css";

const RequestSendList = () => {
  return (
    <div className="users-card">
      {Users.map((user) => (
        <User key={user._id} data={user} textButton="delete request" />
      ))}
    </div>
  );
};

export default RequestSendList;
