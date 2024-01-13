import {useState} from "react";

const Throne = () => {
    
    const fetcher = async () => {
    const res = await fetch("/api/auth", {
      method: 'POST', 
      headers: {
    'Content-Type': 'application/json',
      },
      body: JSON.stringify({"token" : sessionStorage.token}) ,
    })
    return res;
    }

    const [flag, setFlag] = useState("");

    async function auth(){

      const initRes = await fetcher();
      const res = await initRes.json();

      if(res.status !== 200){
          alert("how dare you pest, stepping on my throne!");
          window.location.href = "/";
          return;
      };
      setFlag(res.data.flag);
    }
    auth();
    
    


    return(
    <>
    { flag !== "" && <div className="max-w-screen min-h-screen flex flex-col items-center justify-center">
        <img src="/tsun-nadenka.png" alt="nadenka"
        className=" shadow-sm rounded-[3px] w-[900px] h-[900px]" longdesc="Property of MyticalCat. Any commercial and or personal usage to gain profit is prohibited."/>
        <h1 className="text-3xl">f-fine!,here's the flag. you'd better buy me strawberry ice cream! </h1>
        <h1><span className="bg-yellow-500">{flag}</span></h1>
        
    </div>}
    </>
    )
}
export default Throne;
