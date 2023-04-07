import React from "react";
import "./user.css";
import Button from "../Button/Button";
// import { ShopContext } from "../../context/shop-context";

const User = (props) => {
  const { firstName, lastName } = props.data;
  //   const { follow } = useContext(ShopContext);

  return (
    <div className="user">
      {/* <img src={userImage} alt="" /> */}
      <div className="username">
        <span>
          {firstName} {lastName}
        </span>
      </div>
      <Button text={"Remove"} />
    </div>
  );
};

export default User;
