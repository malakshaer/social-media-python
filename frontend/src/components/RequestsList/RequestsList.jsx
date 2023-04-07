import { Users } from "../../users";
import User from "../User/User";
import "./requestslist.css";

const RequestsList = () => {
  return (
    <div className="users-card">
      {Users.map((user) => (
        <User key={user._id} data={user} textButton="accept" />
      ))}
    </div>
  );
};

export default RequestsList;
