package main

import "fmt"

type Post struct {
	Id      int
	Content string
}

func main() {
	oldPosts := []Post{
		Post{Id: 0, Content: "c0_old"},
		Post{Id: 1, Content: "c1_old"},
		Post{Id: 2, Content: "c2_old"},
	}
	newPosts := []Post{
		Post{Id: 0, Content: "c0_new"},
		Post{Id: 2, Content: "c2_new2"},
		Post{Id: 3, Content: "c3_new3"},
	}

	createPosts, updatePosts, deletePosts := getDiffPosts(oldPosts, newPosts)
	fmt.Println(createPosts)
	fmt.Println(updatePosts)
	fmt.Println(deletePosts)
}

func getDiffPosts(old []Post, new []Post) ([]Post, []Post, []Post) {
	_create := []Post{}
	_update := []Post{}
	for _, newPost := range new {
		isCreate := true
		for oldI, oldPost := range old {
			if newPost.Id == oldPost.Id {
				isCreate = false
				_update = append(_update, newPost)
				old = append(old[:oldI], old[oldI+1:]...)
				break
			}
		}
		if isCreate {
			_create = append(_create, newPost)
		}
	}

	return _create, _update, old
}
