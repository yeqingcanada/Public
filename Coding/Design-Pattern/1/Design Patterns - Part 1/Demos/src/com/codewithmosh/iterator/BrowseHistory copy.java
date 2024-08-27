package com.codewithmosh.iterator;

import java.util.ArrayList;
import java.util.List;

public class BrowseHistory {
  private List<String> urls = new ArrayList<>();


  public void push(String url) {
    urls.add(url);
  }

  public String pop() {
    var lastIndex = urls.size() - 1;
    var lastUrl = urls.get(lastIndex);
    urls.remove(lastUrl);

    return lastUrl;
  }

  public Iterator createIterator() {
    // here need to pass a reference to a history object, the history object, we want to iterate over
    return new ListIterator(this);
  }

  public class ListIterator implements Iterator {
    private BrowseHistory history;
    private int index;

    public ListIterator(BrowseHistory history) {
      this.history = history;
    }

    @Override
    public boolean hasNext() {
      return (index < history.url.size());
    }

    @Override
    public String current() {
      return history.urls.get(index);
    }

    @Override
    public void next() {
      index++;
    }
  }
}