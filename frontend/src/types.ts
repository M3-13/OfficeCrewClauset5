export interface User {
  id: number;
  email: string;
  created_at: string;
}

export type Category =
  | "tops"
  | "bottoms"
  | "outerwear"
  | "shoes"
  | "accessories"
  | "dresses";

export interface ClothingItem {
  id: number;
  name: string;
  category: Category;
  description: string | null;
  image_url: string | null;
  created_at: string;
}

export interface Outfit {
  id: number;
  name: string;
  items: ClothingItem[];
  created_at: string;
}

export interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
}
