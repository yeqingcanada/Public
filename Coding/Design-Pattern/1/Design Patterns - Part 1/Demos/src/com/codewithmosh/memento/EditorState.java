package com.codewithmosh.memento;

public class EditorState {
  private final String content;

  public EditorState(String content) {
    this.content = content;
  }

  public String getContent() {
    return content;
  }

// *********************************************
  private final String title;

  public EditorState(String content, String title) {
    this.content = content;
    this.title = title;
  }

  public String getTitle() {
    return title;
  }
}
