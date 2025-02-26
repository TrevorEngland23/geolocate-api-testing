$(document).ready(function () {
    $.getJSON("https://api.ipify.org?format=json", function(ipData) {
        $.getJSON(`http://localhost:3000/get-ip-info?ip=${ipData.ip}`, function (data) {
            $("#ip").text(data.ip_address);
        $("#country").text(data.country);
        $("#city").text(data.city);
        $("#state").text(data.region);
        $("#isp").text(data.connection?.autonomous_system_organization || "N/A");
        $("#longitude").text(data.longitude);
        $("#latitude").text(data.latitude)
    });
});
});