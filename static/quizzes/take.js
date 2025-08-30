(function(){
  const form = document.getElementById("quiz-form");
  const progress = document.getElementById("progress");
  if (!form) return;

  // update progress when answers change
  form.addEventListener("change", () => {
    const fieldsets = Array.from(form.querySelectorAll("fieldset"));
    const answered = fieldsets.filter(fs => {
      const inputs = fs.querySelectorAll("input");
      return Array.from(inputs).some(inp => (inp.type === "radio" || inp.type === "checkbox") && inp.checked);
    }).length;
    const pct = Math.round(100 * answered / Math.max(fieldsets.length,1));
    if (progress) progress.value = pct;
  });

  // submit via fetch
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const url = window.location.pathname.replace("/take/","/submit/");
    const resp = await fetch(url, { method: "POST", headers: { "X-Requested-With": "XMLHttpRequest" }, body: data });
    const json = await resp.json();
    if (json.ok) window.location.href = `/submission/${json.submission_id}/`;
    else alert(json.error || "Submission failed");
  });
})();
