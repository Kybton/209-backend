function editUser(button) {
    let row = button.parentNode.parentNode;
    console.log(row.cells[0].innerHTML);
    const HTTP = new XMLHttpRequest();
    const url = "http://localhost:5000/admin/login";
    HTTP.open("GET", url);
    HTTP.send();
}

document.addEventListener("DOMContentLoaded", function () {
    const editForm = document.getElementById("edit-form");
    const editId = document.getElementById("edit-id");
    const editName = document.getElementById("edit-name");
    const editEmail = document.getElementById("edit-email");
    const editAdmin = document.getElementById("edit-admin");
    
    const editButtons = document.querySelectorAll(".edit-btn");

    editButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();
            
            const row = button.closest("tr");
            const id = row.cells[0].textContent;
            const name = row.cells[1].textContent;
            const email = row.cells[2].textContent;
            const is_admin = row.getAttribute("data-admin") === "1";
            
            editId.value = id;
            editName.value = name;
            editEmail.value = email;
            editAdmin.checked = is_admin;
      });
    });
  });