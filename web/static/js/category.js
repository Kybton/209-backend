document.addEventListener("DOMContentLoaded", function () {
    const editId = document.getElementById("edit-id");
    const editName = document.getElementById("edit-name");
    
    const editButtons = document.querySelectorAll(".edit-btn");

    editButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();
            
            const row = button.closest("tr");
            const id = row.cells[0].textContent;
            const name = row.cells[1].textContent;
            
            editId.value = id;
            editName.value = name;
      });
    });

    const form = document.getElementById("my-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
    
        const clickedButton = document.querySelector("button[type=submit]:focus");
        const action = clickedButton.getAttribute("value");
    
        if (action === "add") {
            editId.value = null;
        }
    
        form.submit();
    });
});