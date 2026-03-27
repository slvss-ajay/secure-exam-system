function submitAnswer() {
    let answer = document.getElementById("answer").value;

    fetch("/evaluate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({answer: answer})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("enc").innerText = data.encrypted;
        document.getElementById("score").innerText = data.score;

        let logs = document.getElementById("logs");
        logs.innerHTML = "";

        data.logs.forEach(log => {
            let li = document.createElement("li");
            li.innerText = `Score: ${log.score} | ${log.time}`;
            logs.appendChild(li);
        });
    });
}