function deleteNote(noteId) {
  fetch("/note/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/note";
  });
}
