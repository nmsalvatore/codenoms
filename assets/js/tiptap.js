import { Editor } from "@tiptap/core";
import Placeholder from "@tiptap/extension-placeholder";
import StarterKit from "@tiptap/starter-kit";

document.addEventListener("DOMContentLoaded", () => {
  // tiptap editor for new posts
  const newPostForm = document.querySelector("#new_post_form");
  if (newPostForm) {
    const editor = new Editor({
      element: document.querySelector(".tiptap-editor"),
      extensions: [
        StarterKit,
        Placeholder.configure({
          placeholder: "Say something",
        }),
      ],
    });

    newPostForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const contentInput = document.getElementById("tiptap_content");
      const content = editor.getHTML();
      contentInput.value = content;
      newPostForm.submit();
    });
  }

  // tiptap editor for editing posts
  const editPostForm = document.querySelector("#edit_post_form");
  if (editPostForm) {
    const editor = new Editor({
      element: document.querySelector(".tiptap-editor"),
      extensions: [
        StarterKit,
        Placeholder.configure({
          placeholder: "Say something",
        }),
      ],
      content: postContent,
    });

    editPostForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const contentInput = document.getElementById("tiptap_content");
      const content = editor.getHTML();
      contentInput.value = content;
      editPostForm.submit();
    });
  }
});
