function openAndCloseNav() 
{
    let sidebar = document.getElementById("mySidebar").style.width;
    let main = document.getElementById("main").style.marginLeft;
    
    if (sidebar === "150px" && main === "140px")
    {
        document.getElementById("mySidebar").style.width = "50px";
        document.getElementById("main").style.marginLeft = "40px";
        document.querySelector(`.openbtn`).innerHTML = "&raquo";
    }  
    else
    {
        document.getElementById("mySidebar").style.width = "150px";
        document.getElementById("main").style.marginLeft = "140px";
        document.querySelector(`.openbtn`).innerHTML = "&laquo";
    }
     
}