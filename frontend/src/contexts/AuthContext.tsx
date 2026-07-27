import { createContext, useContext, useState, type ReactNode } from "react";
import type { AuthState, User } from "../types";

interface AuthContextType extends AuthState {
  login: (_email: string, _password: string) => Promise<void>;
  register: (_email: string, _password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);

  const login = async (_email: string, _password: string) => {};
  const register = async (_email: string, _password: string) => {};
  const logout = () => {
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated: user !== null,
        login,
        register,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth(): AuthContextType {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return ctx;
}
