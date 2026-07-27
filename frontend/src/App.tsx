import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import AuthGuard from "./components/AuthGuard";
import Navbar from "./components/Navbar";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import GalleryPage from "./pages/GalleryPage";
import OutfitsPage from "./pages/OutfitsPage";
import OutfitCreatorPage from "./pages/OutfitCreatorPage";

export default function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Navbar />
        <Routes>
          <Route path="/" element={<Navigate to="/gallery" replace />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route element={<AuthGuard />}>
            <Route path="/gallery" element={<GalleryPage />} />
            <Route path="/outfits" element={<OutfitsPage />} />
            <Route path="/outfits/create" element={<OutfitCreatorPage />} />
          </Route>
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}
