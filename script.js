function calculateWeights() {
    const weightLifted = document.getElementById("weight").value;
    const reps = document.getElementById("reps").value;
  
    if (weightLifted <= 0 || reps <= 0) {
      alert("Please enter a valid weight and number of reps.");
      return;
    }
  
    const oneRepMax = Math.round(weightLifted * (1 + (reps / 30)));
    const weights = [];
  
    for (let i = 1; i <= 15; i++) {
      const weight = Math.round(oneRepMax * (1 - (i / 30)));
      weights.push(weight);
    }
  
    document.getElementById("one-rep-max").textContent = oneRepMax + " lbs";
  
    const tableBody = document.getElementById("weights-table-body");
    tableBody.innerHTML = ""; // clear any previous rows
  
    for (let i = 1; i <= 15; i++) {
      const row = document.createElement("tr");
      const repCell = document.createElement("td");
      repCell.textContent = i;
      row.appendChild(repCell);
      const weightCell = document.createElement("td");
      weightCell.textContent = weights[i - 1] + " lbs";
      row.appendChild(weightCell);
      tableBody.appendChild(row);
    }
  }
  