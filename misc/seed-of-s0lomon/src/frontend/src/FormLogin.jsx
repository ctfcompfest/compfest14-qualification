

const FormLogin = ({ header, form_id, index, isNight }) => {
  const showPassword = () => {
    const brr = document.getElementById(`password${index}`);
    if (brr.type === "password") {
      brr.type = "text";
    } else {
      brr.type = "password";
    }
  };

  const fetcher = async (payload) => {

    const res = await fetch("/api/validate", {
      method: 'POST', 
      headers: {
    'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),

    })
    return res;
  } 

  const submitHandler = (e) => {
    e.preventDefault();
    validator({
      username : e.target[0].value,
      password : e.target[1].value,
      offering : e.target.id,
      isNight : isNight
    });
  };

  const validator = async (payload) => {
    const initRes = await fetcher(payload);
    const res = await initRes.json();
    
   if(res.status === 200){
    sessionStorage.setItem("credentials", `{user : ${res.data.user}, pass : ${res.data.pass}}`);
    sessionStorage.setItem("token", res.data.token);
    window.location.href = "/throne";
   }else if(res.status === 401){
    alert("That's not what i want.");
   }else if(res.status === 429){
    alert("how dare you spamming my throne with your sinful requests! (cooldown 3 mins)");
   }
  }


  return (
    <form
      onSubmit={(e) => submitHandler(e)}
      method="POST"
      id={form_id}
      action="urll"
      className=" flex flex-col gap-y-3 rounded-xl border shadow-sm w-full md:w-1/3 bg-white "
    >
      <h1 className="text-3xl bg-blue-500 text-white rounded-t-xl text-center py-2">
       {header}
      </h1>
      <div className="flex flex-col w-full gap-y-2 px-4 pb-4">
        <div className="flex flex-col">
          <label className="text-lg mb-1" htmlFor="username">
            username
          </label>
          <input
            name="username"
            id="username"
            type="text"
            className=" border p-2 rounded-sm"
          ></input>
        </div>

        <div className="flex flex-col">
          <label className="text-lg mb-1" htmlFor="password">
            password
          </label>
          <input
            name="password"
            id={`password${index}`}
            type="password"
            className=" border p-2 rounded-sm"
          ></input>
        </div>

        <div>
          <input
            type="checkbox"
            onClick={() => showPassword()}
            className="w-4 h-4 mr-4"
          />
          <label htmlFor="show-password">show password</label>
        </div>
        <button
          className="w-1/4 px-4 py-2 shadow-sm rounded-md border text-gray-500 self-center mt-4 hover:border-lime-400 hover:bg-lime-400 hover:text-lime-700 transition-all duration-100"
          type="submit"
        >
          login
        </button>
      </div>
    </form>
  );
};

export default FormLogin;
