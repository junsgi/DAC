const get = async (t1, t2, t3) => {
    let result = await fetch("http://127.0.0.1:8000",{
        headers : {
            "Content-Type" : "application/json"
        },
        method : "post",
        body : JSON.stringify({
            table1 : t1,
            table2 : t2,
            table3 : t3
        })
    })
    .then(res => res.json())
    .then(res => console.log(res))
}