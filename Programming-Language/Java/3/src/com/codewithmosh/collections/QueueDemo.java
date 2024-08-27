package com.codewithmosh.collections;

import java.util.ArrayDeque;
import java.util.Queue;

public class QueueDemo {
  public static void show() {
    Queue<String> queue = new ArrayDeque<>();
    queue.add("c");
    queue.add("a");
    queue.add("b");
    // b -> a -> c

    var front = queue.remove();

    front = queue.element();

    System.out.println(front);
    System.out.println(queue);

    // We have alternative methods that don't
    // throw an exception:

    // offer() similar to add()
    // poll() similar to remove()
    // peek() similar to element()

    // 当一个 queue 满了的时候，add 会抛出异常，offer 会返回 false
    // 当一个 queue 空了的时候，element throw exception, peek 返回 null
  }
}
