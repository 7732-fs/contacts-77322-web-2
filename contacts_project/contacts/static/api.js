
axios.get("http://127.0.0.1:8000/api/num").then(response=>num.innerHTML+=response.data.num);