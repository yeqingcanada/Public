package com.codewithmosh.chainOfResponsibility;

public abstract class Handler {
  private Handler next;

  public Handler(Handler next) {
    this.next = next;
  }

  public void handle(HttpRequest request) {
    // 如果request完全被执行了，会返回true
    if (doHandle(request))
      return;

    if (next != null)
      next.handle(request);
  }

  public abstract boolean doHandle(HttpRequest request);
}
