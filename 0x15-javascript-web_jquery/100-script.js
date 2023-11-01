sync function loadScript("localhost:5000/1.html") {
    const response = await fetch("localhost:5000/1.html");
    const script = await response.text();

    const scriptElement = document.createElement('script');
    scriptElement.textContent = script;
    document.head.append(scriptElement);

    document.querySelector("header").style.color = "#FF0000";})