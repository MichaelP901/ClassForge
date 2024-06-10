function openModalAddClass()
{
    document.getElementById("modalBackDropAdd").style.display = "flex";
}

function openModalDeleteClass()
{
    if (document.getElementById("class-name"))
    {
        document.getElementById("modalBackDropDelete").style.display = "flex";
    }
}

function closeModalClass()
{
    if (document.getElementById("modalBackDropAdd").style.display == "flex")
    {
        document.getElementById("modalBackDropAdd").style.display = "none";
    }
    else
    {
        document.getElementById("modalBackDropDelete").style.display = "none";
    }
}

function openModalAddAssignments()
{
    document.getElementById("modalBackDropAddAssignments").style.display = "flex";
}

function openModalDeleteAssignments()
{
    if (document.getElementById("class-name"))
    {
        document.getElementById("modalBackDropDeleteAssignments").style.display = "flex";
    }
    
}

function closeModalAssignments()
{
    if (document.getElementById("modalBackDropAddAssignments").style.display == "flex")
    {
        document.getElementById("modalBackDropAddAssignments").style.display = "none";
    }
    else
    {
        document.getElementById("modalBackDropDeleteAssignments").style.display = "none";
    }
}



function showAssignments(assignmentsId) 
{
    // Hide all assignment sections
    var assignmentsSections = document.getElementsByClassName('assignments');
    for (var i = 0; i < assignmentsSections.length; i++) {
        assignmentsSections[i].style.display = 'none';
    }
    // Show the selected assignment section
    document.getElementById(assignmentsId).style.display = 'block';
}




