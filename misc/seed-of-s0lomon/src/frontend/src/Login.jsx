import { MdOutlineModeNight } from "react-icons/md";
import { WiDaySunny } from "react-icons/wi";
import { useState } from "react";

import FormLogin from "./FormLogin";

const Login = () => {
  const [isDark, setIsDark] = useState(false);

  const changeMode = () => {
    setIsDark(!isDark);
  };
  return (
    <>
      <div
        className={
          "relative text-xl md:text-3xl lg:text-5xl text-center py-5 transition-all duration-200 ease-in " +
          (isDark ? "bg-slate-500" : "bg-red-300")
        }
      >
        <h1
          className={
            "transition-all duration-200 ease-in " +
            (isDark ? "text-lime-300" : "")
          }
        >
          Welcome to s0lomon's gate
        </h1>
        <div
          className={
            "absolute flex flex-row items-center right-10 bottom-6 w-16 h-10  rounded-full shadow-inner filter drop-shadow-sm transition-all duration-100 " +
            (isDark ? "bg-lime-500" : "bg-red-50")
          }
        >
          <button
            onClick={() => changeMode()}
            className={" flex items-center justify-center ml-1 w-9 h-9 rounded-full bg-slate-200 shadow-sm transition " + (isDark ? "translate-x-5" : "")}
          >
            {isDark && <MdOutlineModeNight className="w-5 h-5" />}
            {!isDark && <WiDaySunny className="w-6 h-6" />}
          </button>
        </div>
      </div>
      <div className={"App max-w-screen min-h-screen flex flex-col items-center py-20 transition=all duration-200 ease-in " +(isDark ? "bg-slate-800" : "bg-slate-100")}>
        <div className="flex flex-col items-center w-full gap-y-[100px]">
          <FormLogin
            header={"I have diamonds for you nadenka! Now gimme the flag"}
            form_id="diamond"
            index={0}
            isNight={isDark}
          />
          <FormLogin
            header={"why won't you gimme the flag :("}
            form_id="crowns"
            index={1}
            isNight={isDark}
          />
          <FormLogin
            header={"nadenka i'll buy you an ice cream"}
            form_id="gl1da"
            index={2}
            isNight={isDark}
          />
          <FormLogin
            header={"GIVE ME THE FLAG. I'll give you my soul"}
            form_id="soul"
            index={3}
            isNight={isDark}
          />
        </div>
      </div>
    </>
  );
};

export default Login;
