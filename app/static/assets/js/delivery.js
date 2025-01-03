

document.addEventListener("DOMContentLoaded", function () {
    const cityInput = document.getElementById("id_city");
    const departmentSelect = document.getElementById("id_department");

    cityInput.addEventListener("change", function () {
        const city = cityInput.value;
        if (city) {
            fetch(`/orders/get_departments/?city=${encodeURIComponent(city)}`)
                .then(response => response.json())
                .then(data => {
                    departmentSelect.innerHTML = '<option selected disabled value="">Choose...</option>';
                    if (Array.isArray(data) && data.length > 0) {
                        data.forEach(department => {
                            const option = document.createElement("option");
                            option.value = department.Description; // Используем описание в качестве значения
                            option.textContent = department.Description; // Отображаем описание
                            departmentSelect.appendChild(option);
                        });
                    } else {
                        departmentSelect.innerHTML = '<option selected disabled value="">No departments found</option>';
                    }
                })
                .catch(error => {
                    console.error("Error fetching departments:", error);
                    departmentSelect.innerHTML = '<option selected disabled value="">Error loading departments</option>';
                });
        }
    });
});